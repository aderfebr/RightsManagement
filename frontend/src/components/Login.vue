<template>
  <div class="login-bg">
    <div class="login-container">
      <h1>登录</h1>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">用户名:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">密码:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div class="form-actions">
          <el-button @click="back()">返回</el-button>
          <el-button type="primary" @click="submit()">注册</el-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { getCurrentInstance,ref } from 'vue';
import router from '..';
const {proxy} = getCurrentInstance()

var username=ref("");
var password=ref("");

function submit(){
  if(username.value==""||password.value==""){
    window.alert("信息不能为空");
  }
  else{
  proxy.$http.post("http://localhost:8000/api/login/",{
    'username':username.value,
    'password':password.value,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    else{
      localStorage.setItem('username',res.data.username);
      localStorage.setItem('token',res.data.token);
    }
  });
  setTimeout(() => {
    router.push('/user');
  }, 200);}
}

function back(){
  router.push('/user');
}
</script>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

.login-bg {
  background: linear-gradient(to right, #74ebd5, #acb6e5);
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  position: fixed; 
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.login-container {
  max-width: 500px;
  margin: 10% auto;
  padding: 20px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}

h1 {
  text-align: center;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #333;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-actions {
  text-align: right;
}
</style>

