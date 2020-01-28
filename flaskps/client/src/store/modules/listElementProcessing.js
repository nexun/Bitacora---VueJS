import Vue from 'vue'

export default{
    state: {
        processing: {}
    },
    getters: {
        processing: state => id => state.processing[id]
    },
    actions: {
        startProcessing({commit}, id) {
            commit('startProcessing', id)
        },
        stopProcessing({commit}, id) {
            commit('stopProcessing', id)
        },
        isProcessing({commit}, id) {
            return state.processing[id]
        }
    },
    mutations: {
        startProcessing(state, id) {
            Vue.set(state.processing, id, true)
        },
        stopProcessing(state, id) {
            Vue.set(state.processing, id, false)
        }
    }
}