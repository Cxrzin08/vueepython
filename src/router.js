import { createRouter, createWebHistory } from 'vue-router'
import NovoUsuario from './components/NovoUsuario.vue'
import ListaUsuarios from './components/ListaUsuarios.vue'

const routes = [
  { path: '/', component: NovoUsuario, name: 'Home' },
  { path: '/usuarios', component: ListaUsuarios, name: 'Users' }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router