<template>
  <div class="login-bg">
    <div class="login-container">
      <h1>注册</h1>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">用户名:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">密码:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div class="form-group">
          <label for="groupid">角色id:</label>
          <input type="text" id="groupid" v-model="groupid" required>
        </div>
        <div class="form-group">
          <label for="groupname">角色名:</label>
          <input type="text" id="groupname" v-model="groupname" required>
        </div>
        <div class="form-actions">
          <button @click="submit">登录</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { getCurrentInstance,ref } from 'vue';
import router from '..';
const {proxy} = getCurrentInstance()

var username=ref();
var password=ref();
var groupid=ref();
var groupname=ref();

function submit(){
  proxy.$http.post("http://localhost:8000/api/register/",{
    'username':username.value,
    'password':password.value,
    'groupid':groupid.value,
    'groupname':groupname.value,
  },{
    headers: {'Content-Type': 'multipart/form-data'},
  });
  setTimeout(() => {
    router.push('/user');
  }, 200);
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

button {
  padding: 10px 20px;
  background-color: #409eff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #555;
}

a{
  color: #fff;
  text-decoration: none;
}
</style>

