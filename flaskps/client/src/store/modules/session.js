import axios from 'axios'

export default{
    state: {
        status: 0, // 0 = 'not yet' , 1 = 'pending' , 2 = 'done'
        user: null
    },
    getters: {
        getStatus(state) {
            return state.status
        },
        getUser(state) {
            return state.user
        }
    },
    actions: {
        async reset({commit}) {
            commit('setStatus', 0)
        },
        async start({commit}) {
            commit('setStatus', 1)
        },
        async finish({commit}) {
            commit('setStatus', 2)
        },
        async saveUser({commit}, user) {
            commit('setUser', user)
        },
        async newUser({dispatch, commit}, credentials) {    
            await dispatch('start')
            try {
                const response = await axios.post('/auth', credentials)
                await dispatch('saveUser', response.data.user)
                await dispatch('finish')
            } catch (error) {
                await dispatch('reset')
                throw error
            }      
        },
        destroyUser({commit}) {
            commit('setStatus', 0)
            commit('setUser', null)
        }
    },
    mutations: {
        setStatus(state, status) {
            state.status = status
        },
        setUser(state, user) {
            state.user = user
        }
    }
}