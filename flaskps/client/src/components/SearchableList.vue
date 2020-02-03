<template>
<div>
    <div class="card shadow col-lg-12 p-0">
        <div class="card-header p-0">
            <form @submit.prevent="filter" id="sercheable_form">
                <div class="row">
                    <div class="col-md-6 text-center">
                        <h4 class="list-title text-muted py-1 pl-3 m-0" v-if=listTitle>{{ listTitle }}</h4>
                    </div>
                    <div class="input-group col-md-6">
                        <input v-model="query_input" :disabled="searching || disabled" type="text" class="search-bar-input form-control form-control" @focus="query_input=''" placeholder="Buscar">
                        <div class="input-group-append">
                            <button type="submit" class="btn btn-custom-light py-0 px-3" :disabled="searching || disabled">
                                <search-icon v-if="!searching" size="1.5x" class="custom-class" />
                                <span class="spinner-border spinner-border-sm" role="status" v-if="searching"></span>
                            </button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
        <div class="card-body p-0">
            <table class="table-hover custom-table">
                <thead class="thead-dark">
                    <tr>
                        <th :key="column.name" v-for="column in columns" scope="col" class="py-3">
                            {{ column | capitalize }}
                        </th>
                    </tr>
                </thead>
                <component :is="listName" :rows="rows" @reload="reload"/>
            </table>
        </div>
        <div class="card-footer text-center p-1">
            <nav>
                <ul class="pagination justify-content-center m-0">
                    <li class="page-item" :class="{disabled: currentPage == 1}">
                        <a class="page-link" href="#" @click="setPage(1)">Primera</a>
                    </li>
                    <li class="page-item" :class="{disabled: currentPage == 1}">
                        <a class="page-link" href="#" @click="setPage(currentPage - 1)">&laquo;</a>
                    </li>
                    <li class="page-item active">
                        <a class="page-link" href="#">{{ currentPage }}</a>
                    </li>
                    <li class="page-item" :class="{disabled: currentPage == totalPages}">
                        <a class="page-link" href="#" @click="setPage(currentPage + 1)">&raquo;</a>
                    </li>
                    <li class="page-item" :class="{disabled: currentPage == totalPages}">
                        <a class="page-link" href="#" @click="setPage(totalPages)">Última</a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</div>
</template>

<script>
import { SearchIcon } from 'vue-feather-icons'
import axios from 'axios'
import Fuse from 'fuse.js'

export default {
    name: 'SearchableList',
    components: {
        SearchIcon
    },
    props: [
        'listName',
        'listTitle',
        'columns',
        'endpoint',
        'options',
        'noAutoSearch',
        'disabled'
    ],
    data() {
        return {
            paginationNumber: null,
            query_input: '',
            searching: false,
            result: [],
            filtered: [],
            currentPage: 1
        }
    },
    computed: {
        start: function() {
            return this.paginationNumber * (this.currentPage - 1)
        },
        stop: function() {
            return this.start + this.paginationNumber
        },
        rows: function() {
            return this.filtered.slice(this.start, this.stop)
        },
        totalPages: function() {
            const total = Math.ceil(this.filtered.length / this.paginationNumber)
            return total ? total : 1
        }
    },
    methods: {
        search() {
            this.searching = true

            axios.get('/configuration/pagination')
                .then(response => {
                    this.paginationNumber = parseInt(response.data.config_options_items_per_page)
                    axios.get(this.endpoint)
                        .then(response => {
                            this.query_input = ''
                            this.result = response.data
                            this.filtered = this.result
                            this.setPage(1)
                        })
                        .catch(error => {})
                })
                .catch(error => {})
                .finally(() => this.searching = false)
        },
        setPage(pageNumber) {
            this.currentPage = parseInt(pageNumber)
        },
        filter() {
            if (this.query_input) {
                const fuse = new Fuse(this.result, this.options)
                this.filtered = fuse.search(this.query_input)
                this.setPage(1)
            } else
                this.search()
        },
        reset() {
            this.result = []
            this.filtered = []
        },
        remove(id) {
            this.filtered = this.filtered.filter(element => element.id != id)
            this.result = this.filtered
        },
        reload(){
            this.$emit("reload",true)
        }
    },
    created() {
        if (!this.noAutoSearch)
            this.search()
    }
}
</script>

<style scoped>
.search-bar-input {
    border: .1rem solid #333;
}

.search-column-icon {
    transform: rotate(0deg);
    height: 1em;
    width: 1em;
}
#sercheable_form{
    background-color: #fb6363;
    padding: 7px;
    /*jejeje*/
}
@media screen and (max-width: 800px){
    #sercheable_form{
    padding: 15px;
    /*jejeje*/
}
}
.order-button {
    color: grey;
    text-decoration: none;
}

.asc {
    color: red;
    transform: rotate(180deg);
}

.desc {
    color: red;
    transform: rotate(0deg);
}

.form-control:focus {
    outline: none;
    border-color: #945a5f !important;
    box-shadow: 0 0 0 0.2rem #c5757b !important;
}

.clickable-th:hover {
    border-bottom: 3px solid #69262c !important;
}

.search-icon {
    width: 1em;
    height: 1em;
    margin-bottom: 2px;
    margin-left: 5px;
}

.search-icon-info {
    position: absolute;
    top: 0;
    left: 0;
    margin: 0;
    color: #333;
}

.card-header {
    border-bottom: none;
}

.card-footer {
    border-top: none;
}

.list-title {
    letter-spacing: .075em;
    text-transform: uppercase;
}

.page-item.active .page-link {
    color: #fff !important;
    background-color: #69262c;
    border-color: #69262c;
}

.page-link:focus {
    -webkit-box-shadow: 0 0 0 0.2rem #c5757b !important;
    box-shadow: 0 0 0 0.2rem #c5757b !important;
}

.page-item.disabled .page-link {
    color: #6c757d !important;
}
</style>


<style>
.custom-table {
    border: none;
    border-collapse: collapse;
    margin: 0;
    padding: 0;
    width: 100%;
}

.custom-table thead {
    border-bottom: 2px solid #ccc;
}

.custom-table tr {
    background-color: #fcfcfc;
    border: 1px solid #ddd;
    padding: .35em;
    border-left: none;
    border-right: none;
}

.custom-table th,
.custom-table td {
    padding: .625em;
    text-align: center;
}

.custom-table th {
    font-size: .85em;
    letter-spacing: .1em;
    text-transform: uppercase;
}

.custom-table a {
    font-weight: 500;
    text-decoration: none;
}

.custom-table a,
.page-link {
    color: #69262c !important;
}

.custom-table a:hover,
.page-link:hover {
    color: #69262c !important;
}


@media screen and (max-width: 1200px) {
    .custom-table {
        border: 0;
    }

    .custom-table thead {
        border: none;
        clip: rect(0 0 0 0);
        height: 1px;
        margin: -1px;
        overflow: hidden;
        padding: 0;
        position: absolute;
        width: 1px;
    }

    .custom-table tr {
        display: block;
        border: 1px solid #ccc;
        box-shadow: 5px 5px #eee;
        margin: 0.75em;
    }

    .custom-table td {
        border-bottom: 1px solid #ddd;
        display: block;
        font-size: .8em;
        text-align: right;
    }

    .custom-table td::before {
        content: attr(data-label);
        float: left;
        font-weight: bold;
        text-transform: uppercase;
    }

    .custom-table td:last-child {
        border-bottom: 0;
    }
}
</style>
