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
        :unique-opened=true
        :router=true
        >
          <el-menu-item v-for="item in index" :index="item.index"><el-icon><component :is="item.icon" /></el-icon>{{ item.label }}</el-menu-item>
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
import { getCurrentInstance,onMounted,ref } from 'vue';
import {useRouter} from 'vue-router'
const {proxy} = getCurrentInstance()

var activeIndex=useRouter().currentRoute.value.path;
var index=ref()

function getmenu(){
  proxy.$http.get("http://localhost:8000/api/getmenu/").then((res)=>{
  index.value=res.data;
  });
}

onMounted(()=>{
  getmenu();
})
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