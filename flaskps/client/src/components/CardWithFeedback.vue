<template>
<div class="card shadow col-lg-10 p-0">
    <div class="card-header d-flex align-items-center">
        <h5 class="mb-0">{{ cardData.title }}</h5>
        <div class="feedback-popper-container">
            <transition name="popper-shown">
                <div v-if="ok" class="feedback-popper feedback-popper-ok">
                    {{ cardData.msj.ok }}
                </div>
            </transition>
            <transition name="popper-shown">
                <div v-if="error" class="feedback-popper feedback-popper-error">
                    {{ cardData.msj.error }}
                </div>
            </transition>
        </div>
    </div>
    <div class="card-body">
        <component :is="cardData.form" @processing="startProcessing" @ok="processOk" @error="processError" />
    </div>
</div>
</template>

<script>
export default {
    name: 'CardWithFeedback',
    props: [
        'cardData'
    ],
    data() {
        return {
            ok: false,
            error: false
        }
    },
    methods: {
        startProcessing() {
            this.ok = false
            this.error = false
        },
        processOk() {
            this.ok = true
            this.$emit("reload",true)
        },
        processError() {
            this.error = true
        }
    }
}
</script>

<style scoped>
.card {
    margin-bottom: 25px;
}

.card-header {
    border-bottom: 1px solid #69262c;
}

@media(max-width: 767px){
    .card{
        margin-left: 15px
    }
}

.feedback-popper-container {
    position: absolute;
    width: 100%;
    top: 48px;
    right: 0;
    perspective: 1000px;
}

.feedback-popper {
    position: absolute;
    display: inline-block;
    right: 0;
    max-width: 100%;
    padding: .25rem .5rem;
    font-size: 1rem;
    line-height: 1.5;
    color: #fff;
    border-radius: .25rem;
    opacity: 0;
    transform-origin: top center;
}

.feedback-popper-ok {
    background-color: rgba(40,167,69,.9);
}

.feedback-popper-error {
    background-color: rgba(220,53,69,.9);
}

.popper-shown-enter-active {
    animation: popper-fade 5s ease-in-out 1;
}

@keyframes popper-fade {
    0% {
        opacity: 0;
        transform: rotateX(-90deg);
    }
    10%, 70% {
        opacity: 1;
        transform: rotateX(0deg);
    }
    100% {
        opacity: 0;
        transform: rotateX(-90deg);
    }
}
</style>
