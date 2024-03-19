<template>
    <div class="main">
        <Header></Header>
        <div class="title">菜单管理</div>
        <el-divider></el-divider>
        <el-tree class="tree" :data="index" font-size="20px">
          <template #default="{node,data}">
            <span><el-icon><component :is="data.icon" /></el-icon>&ensp;{{ data.label }}&ensp;<el-switch v-model="data.vis"/></span>
          </template>
        </el-tree>
      <br><el-button type="success" @click="submit">确认&ensp;<el-icon><Check /></el-icon></el-button>
    </div>
</template>

<script setup>
import Header from '../components/Header.vue'

var index=[{
  label:"权限管理",
  icon:"Operation",
  vis:true,
  children:[{
    label:"用户管理",
    vis:true,
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

function submit(){
    console.log(index)
}
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