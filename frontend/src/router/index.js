import { createWebHistory, createRouter } from "vue-router";

const routes = [{
        path: "/",
        name: "Home",
        component: () =>
            import ("@/views/Home.vue")
    },
    {
        path: "/login",
        name: "Login",
        component: () =>
            import ("@/views/Login.vue")
    },
    {
        path: "/registration",
        name: "Registration",
        component: () =>
            import ("@/views/Registration.vue")
    },
    {
        path: "/profile",
        name: "Profile",
        component: () =>
            import ("@/views/Profile.vue")
    },
    {
        path: "/logout",
        name: "Logout",
        component: () =>
            import ("@/views/Logout.vue")
    },
    {
        path: "/add_item",
        name: "AddItem",
        component: () =>
            import ("@/views/AddItem.vue")
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;