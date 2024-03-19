<template>
  <el-row style="height: 100vh">
    <el-col :span="4">
      <el-scrollbar class="aside">
        <div class="side-top">权限管理系统</div>
        <el-menu
        boder="none"
        active-text-color="#ffd04b"
        background-color="#427eff"
        text-color="#fff"
        :default-active="activeIndex"
        :router="true"
        >
          <el-sub-menu v-for="item in index">
            <template #title><el-icon><component :is="item.icon" /></el-icon>{{ item.label }}</template>
            <el-menu-item v-for="child in item.children" :index="child.index">{{ child.label }}</el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-scrollbar>
    </el-col>
    <el-col :span="20">
      <router-view></router-view>
      <div style="background: #fff;height: 100%;"></div>
    </el-col>
  </el-row>
</template>

<script setup>
import {useRouter} from 'vue-router'

var activeIndex=useRouter().currentRoute.value.path;

var index=[{
  label:"权限管理",
  icon:"Operation",
  vis:true,
  children:[{
    label:"用户管理",
    vis:false,
    index:"/user",
  },
  {
    label:"角色管理",
    vis:true,
    index:"/role",
  },
  {
    label:"菜单管理",
    vis:true,
    index:"/menu",
  },
  ]
},
{
  label:"功能一",
  icon:"MoreFilled",
  vis:true,
  children:[
    {
    label:"测试一",
    vis:true,
    index:"",
    },
  ]
}];
</script>

<style scoped>
.el-menu{
  border-right: none;
}
.side-top{
  padding: 50px 0;
  font-size: 25px;
  text-align: center;
  color: #fff;
}
.aside {
  background: #427eff;
}
</style>