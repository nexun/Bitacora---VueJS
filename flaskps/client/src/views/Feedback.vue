<template>
<div class="container-fluid text-center">
    <div class="d-flex w-100 h-100 p-3 flex-column">

    <header class="mb-auto">
        <div class="brand text-center">
            <router-link to="/">
                <img src="../assets/img/logo_bitacora.png" alt="Logo Bitacora 2.0"
                class="img-fluid">
            </router-link>
        </div>
    </header>

    <main role="main">
        <h1 class="mb-3">
        {{ title }}
        </h1>
        <p class="mb-3">{{ description }}</p>
        <div class="d-flex justify-content-center">
            <router-link to="/" class="btn btn-lg btn-custom-dark">Home</router-link>
            <button @click="goBack" v-if="!noBacktrack" class="btn btn-lg btn-custom-dark ml-2">Volver</button>
        </div>
    </main>

    <footer class="contact-footer mt-auto">
        <p>También podés <router-link class="contact-link" to="/contacto">contactarte</router-link> con nosotros.</p>
    </footer>


    </div>
</div>
</template>

<script scoped>
export default {
    name: 'Feedback',
    props: [
        'title',
        'description',
        'noBacktrack'
    ],
    methods: {
        goBack() {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
        }
    }
}
</script>

<style scoped>
.container-fluid {
    height: 100%;
    background-color: #333;
    color: #fff;
}

@media (min-width: 48em) {
    .brand {
        float: left;
    }
}

.contact-footer {
    color: rgba(255, 255, 255, .5);
}

.contact-link,
.contact-link:focus,
.contact-link:hover {
    color: #fff;
}
</style>