<template>
    <div class="main">
      <Header></Header>
      <div class="title">菜单管理</div>
      <el-divider></el-divider>
        <!-- <el-tree class="tree" :data="index" font-size="20px">
          <template #default="{node,data}">
            <span><el-icon><component :is="data.icon" /></el-icon>&ensp;{{ data.label }}&ensp;<el-switch v-model="data.vis"/></span>
          </template>
        </el-tree> -->
        <div v-for="item in index"><el-icon><component :is="item.icon" /></el-icon>&ensp;{{ item.label }}&ensp;<el-switch v-model="item.vis"/></div>
      <br><el-button type="success" @click="editmenu">确认&ensp;<el-icon><Check /></el-icon></el-button>
    </div>
</template>

<script setup>
import Header from '../components/Header.vue'
import { getCurrentInstance,onMounted,ref } from 'vue';
const {proxy} = getCurrentInstance()

var index=ref()

function getmenu(){
  proxy.$http.get("http://localhost:8000/api/getmenu/").then((res)=>{
    index.value=res.data;
  });
}

function editmenu(){
  proxy.$http.post("http://localhost:8000/api/editmenu/",{
    'index':JSON.stringify(index.value),
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    location.reload();
  });
}

onMounted(()=>{
  getmenu();
})
</script>

<style scoped>
.title{
    font-size: 20px;  
    background: #fff;
    color: #555;
}
.main{
    background: #fff;
    height: 100%;
    padding: 20px;
}
.tree{
  font-size: 15px;
}
</style>