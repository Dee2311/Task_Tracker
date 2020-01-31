import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import List from "../views/List.vue";
import Task from "../views/Task.vue";
import AddTask from "../views/AddTask.vue";
import AddList from "../views/AddList.vue";

Vue.use(VueRouter);

const routes = [{
        path: "/",
        name: "home",
        component: Home
    },
    {
        path: "/login",
        name: "login",
        component: Login
    },
    {
        path: "/list",
        name: "list",
        component: List
    },
    {
        path: "/task",
        name: "task",
        component: Task
    },
    {
        path: "/addlist",
        name: "addlist",
        component: AddList
    },
    {
        path: "/addtask",
        name: "addtask",
        component: AddTask
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;