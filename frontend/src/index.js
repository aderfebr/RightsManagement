import { createRouter, createWebHistory } from "vue-router"
const Login=()=> import('./components/Login.vue')
const Home=()=> import('./components/Home.vue')
const User=()=> import('./components/User.vue')
const Role=()=> import('./components/Role.vue')
const Menu=()=> import('./components/Menu.vue')

const routes=[
    {
        path:'/login',
        component: Login,
    },
    {
        component: Home,
        children:[
            {
            path:'/user',
            component: User,
            },
            {
            path:'/role',
            component: Role,
            },
            {
            path:'/menu',
            component: Menu,
            },
        ]
    }
]

const router=createRouter({
    history:createWebHistory(),
    routes
})

export default router