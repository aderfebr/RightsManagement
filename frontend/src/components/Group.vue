<template>
    <div class="main">
        <Header></Header>
        <div class="title">角色管理</div>
        <el-divider></el-divider>
        <el-select
          v-model="role"
          placeholder="请选择角色"
          size="large"
          style="width: 300px"
        >
          <el-option
            v-for="item in roles"
            :key="item.key"
            :label="item.label"
            :value="item.key"
          />
        </el-select>
        &ensp;<el-button type="warning" @click="query">查询&ensp;<el-icon><Search /></el-icon></el-button><br><br>
        <el-transfer v-model="auth_check" :data="auth" :titles="['未分配权限', '已分配权限']"/>
        <br><el-button type="success" @click="submit">确认&ensp;<el-icon><Check /></el-icon></el-button>
    </div>
</template>

<script setup>
import Header from '../components/Header.vue'
import { ref } from 'vue'

const role=ref('');

var auth_check=[1]

var roles=[
  {
    key:0,
    label:'student',
  },
  {
    key:1,
    label:'teacher',
  },
];

var auth=[
  {
    key:0,
    label:'访问用户管理',
  },
  {
    key:1,
    label:'访问角色管理',
  },
  {
    key:2,
    label:'访问菜单管理',
  },
]

function query(){
  console.log(role.key)
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
</style>