import { createRouter, createWebHistory } from "vue-router"
const Login=()=> import('./components/Login.vue')
const Register=()=> import('./components/Register.vue')
const Nav=()=> import('./components/Nav.vue')
const User=()=> import('./components/User.vue')
const Role=()=> import('./components/Role.vue')
const Menu=()=> import('./components/Menu.vue')

const routes=[
    {
        path:'/login',
        component: Login,
    },
    {
        path:'/register',
        component: Register,
    },
    {
        component: Nav,
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