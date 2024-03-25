<template>
    <div class="main">
        <Header></Header>
        <div class="title">角色管理</div>
        <el-divider></el-divider>
        <el-select
          v-model="groupid"
          placeholder="请选择角色"
          size="large"
          style="width: 300px"
        >
          <el-option
            v-for="item in options"
            :key="item.groupid"
            :label="item.groupname"
            :value="item.groupid"
          />
        </el-select>
        &ensp;<el-button type="warning" @click="getrights()">查询&ensp;<el-icon><Search /></el-icon></el-button><br><br>
        <el-transfer
          v-model="rightscheck"
          :props="{
            key: 'rightsid',
            label: 'rightsname',
          }"
          :data="rights"
          :titles="['未分配权限', '已分配权限']"
        />
        <br><el-button type="success" @click="editrights()">确认&ensp;<el-icon><Check /></el-icon></el-button>
    </div>
</template>

<script setup>
import Header from '../components/Header.vue'
import { getCurrentInstance,onMounted,ref } from 'vue';
const {proxy} = getCurrentInstance()

var options=ref();
var groupid=ref();
var rights=ref();
var rightscheck=ref();

function getgroup(){
  proxy.$http.get("http://localhost:8000/api/getgroup/").then((res)=>{
    options.value=res.data
  });
}

function getrights(){
  proxy.$http.post("http://localhost:8000/api/getrights/",{
    'groupid':groupid.value,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    else{
      rights.value=res.data.data;
      rightscheck.value=res.data.rights;
    }
  });
}

function editrights(){
  proxy.$http.post("http://localhost:8000/api/editrights/",{
    'groupid':groupid.value,
    'rights':JSON.stringify(rightscheck.value),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  });
}

onMounted(()=>{
  getgroup();
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
</style>