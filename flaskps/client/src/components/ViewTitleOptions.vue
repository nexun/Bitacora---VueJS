<template>
<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom" id="opt">
    <div id="text">
        <h2 class="h2 d-inline">{{ title }}</h2>
        <h4 v-if="subtitle" class="h4 text-muted d-inline"> - {{ subtitle }}</h4>
    </div>
    <div v-if="options" class="btn-toolbar mb-2 mb-md-0" id="opt">
        <router-link class="btn btn-custom-light" v-for="option in options" :key=option.id :to=option.link>
            <component :is="option.icon+'-icon'" size="1.5x" class="custom-class" />
            {{ option.name }}
        </router-link>
    </div>
</div>
</template>

<script>
import { UserPlusIcon, ArrowLeftIcon, FolderPlusIcon, ShieldIcon, PlusIcon, UserCheckIcon, AlertOctagonIcon } from 'vue-feather-icons'

export default {
    name: 'ViewTitleOptions',
    components: {
        UserPlusIcon,
        ArrowLeftIcon,
        FolderPlusIcon,
        ShieldIcon,
        PlusIcon,
        UserCheckIcon,
        AlertOctagonIcon,
    },
    props: [
        'title',
        'subtitle',
        'options'
    ]
}
</script>

<style scoped>
.btn + .btn {
    margin-left: 10px;
}
@media(max-width: 768px){
    
    #opt{
        justify-content: center!important;
    }

    .btn{
            font-size: 0.9rem;
            padding-bottom: 10px;
            border:none;

    }
    #text{
        padding-right: 10px;
        display: inline-grid
    }
}
</style>