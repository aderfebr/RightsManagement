import { createRouter, createWebHistory } from "vue-router"
const Login=()=> import('./components/Login.vue')
const Nav=()=> import('./components/Nav.vue')
const User=()=> import('./components/User.vue')
const Group=()=> import('./components/Group.vue')
const Menu=()=> import('./components/Menu.vue')

const routes=[
    {
        path:'/login',
        component: Login,
    },
    {
        component: Nav,
        children:[
            {
            path:'/user',
            component: User,
            },
            {
            path:'/group',
            component: Group,
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