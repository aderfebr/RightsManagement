<template>
  <div class="header">
    <span>
      <span v-if="!username">当前未登录</span>
      <span v-if="username">当前用户:&ensp;{{username}}</span>
      &ensp;
      <el-dropdown class="setting">
            <el-icon size="25px"><setting/></el-icon>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="login">用户登录</el-dropdown-item>
                <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
      </el-dropdown>
    </span>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import router from '..';

var username=ref(localStorage.getItem('username'))

function login(){
  router.push('/login');
}

function logout(){
  localStorage.removeItem('username');
  localStorage.removeItem('token');
  location.reload();
}
</script>

<style>
.header{
    font-size: 20px;  
    background: #fff;
    height: 40px;
    color: #555;
    text-align: right;
}
.setting{
  outline: none;
  text-decoration: none;
  transition: all 0.2s;
  cursor: pointer;
}
.setting:hover{
  color: #17a2b8;
  transition: all 0.2s;
}
</style>