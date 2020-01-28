import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import session from './modules/session'
import listElementProcessing from './modules/listElementProcessing'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    session,
    listElementProcessing
  },
  plugins: [
    createPersistedState()
  ],
})
