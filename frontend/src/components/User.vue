<template>
    <div class="main">
      <el-dialog
          v-model="addVisible"
          title="添加用户"
          width="500"
          :before-close="handleClose"
        >
          <span>用户名:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.username"
          />
          <span>年龄:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.age"
          />
          <span>地址:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.address"
          />
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="addVisible = false">取消</el-button>
              <el-button type="success" @click="addVisible = false;addsubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <el-dialog
          v-model="editVisible"
          title="修改用户"
          width="500"
          :before-close="handleClose"
        >
          <span>ID:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.userid"
            disabled
          />
          <span>用户名:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.username"
            disabled
          />
          <span>年龄:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.age"
          />
          <span>地址:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.address"
          />
          <br><br><el-button type="primary" @click="pwdclear();">修改密码</el-button>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="editVisible = false">取消</el-button>
              <el-button type="success" @click="editVisible = false;editsubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <el-dialog
          v-model="pwdVisible"
          title="修改密码"
          width="600"
          :before-close="handleClose"
        >
          <span>请输入旧密码:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="oldpwd"
            type="password"
            show-password
          />
          <span>请输入新密码:</span>
          <el-input
            style="padding: 5px 0;"
            v-model="newpwd"
            type="password"
            show-password
          />
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="pwdVisible = false">取消</el-button>
              <el-button type="success" @click="pwdVisible = false;pwdsubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <el-dialog
          v-model="changeVisible"
          title="修改角色"
          width="600"
          :before-close="handleClose"
        >
          <el-transfer
            v-model="groupcheck"
            :props="{
              key: 'groupid',
              label: 'groupname',
            }"
            :data="group"
            :titles="['未分配角色', '已分配角色']"
          />
          <br><el-button type="success" @click="changeVisible = false;editgroup()">确认&ensp;<el-icon><Check /></el-icon></el-button>
        </el-dialog>
        <el-dialog
          v-model="deleteVisible"
          title="删除"
          width="500"
          :before-close="handleClose"
        >
          <span>确定删除用户{{ selected.username }}?</span>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="deleteVisible = false">取消</el-button>
              <el-button type="success" @click="deleteVisible = false;deletesubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <Header></Header>
        <div class="title">用户管理</div>
        <el-divider></el-divider>
        <div v-if="auth">
          <el-row style="font-size: 25px;">
              <el-col :span="20"><el-input size="large" v-model="filter" placeholder="按用户名搜索" style="width: 300px"/>&ensp;<el-button type="primary" @click="getuser">搜索&ensp;<el-icon><Search /></el-icon></el-button><el-button type="danger" @click="filter='';getuser();">清空过滤&ensp;<el-icon><Close /></el-icon></el-button></el-col>
              <el-col :span="4" style="text-align: right;"><el-button type="success" @click="selected={};addVisible=true">添加用户&ensp;+</el-button></el-col>
          </el-row>
          <br>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="ID">
              <template #default="scope">{{ scope.row.userid }}</template>
            </el-table-column>
            <el-table-column label="用户名">
              <template #default="scope">{{ scope.row.username }}</template>
            </el-table-column>
            <el-table-column label="年龄">
              <template #default="scope">{{ scope.row.age }}</template>
            </el-table-column>
            <el-table-column label="地址">
              <template #default="scope">{{ scope.row.address }}</template>
            </el-table-column>
            <el-table-column label="操作" width="300px">
              <template #default="scope">
                <el-button type="warning" @click="editclear(scope.row);">修改用户</el-button>
                <el-button type="primary" @click="changeclear(scope.row);">修改角色</el-button>
                <el-button type="danger" @click="selected=scope.row;deleteVisible=true;">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <br>
          <el-row style="justify-content: center;">
            <el-pagination background layout="prev, pager, next" :page-count="total" v-model:current-page="page" @update:current-page="getuser"/>
          </el-row>
        </div>
        <div v-if="!auth" style="width: 100%;text-align: center;font-size: 25px;color: red;">未授权!</div>
    </div>
</template>

<script setup>
import { getCurrentInstance,onMounted, ref } from 'vue';
import Header from '../components/Header.vue'
const {proxy} = getCurrentInstance()

var tableData=ref();
var auth=ref(false);
var filter=ref();
var page=ref(1);
var total=ref(1);
var selected=ref();

function getuser(){
  proxy.$http.post("http://localhost:8000/api/getuser/",{
    'token':localStorage.getItem("token"),
    'filter':filter.value,
    'page':page.value,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==200){
      tableData.value=res.data.data;
      total.value=res.data.total;
      auth.value=true;
    }
  });
}

var addVisible=ref(false);

function addsubmit(){
  proxy.$http.post("http://localhost:8000/api/adduser/",{
    'username':selected.value.username,
    'age':selected.value.age,
    'address':selected.value.address,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    getuser();
  });
}

var editVisible=ref(false);

function editclear(row){
  editVisible.value=true;
  selected.value=JSON.parse(JSON.stringify(row))
}

function editsubmit(){
  proxy.$http.post("http://localhost:8000/api/edituser/",{
    'userid':selected.value.userid,
    'age':selected.value.age,
    'address':selected.value.address,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    getuser();
  });
}

var pwdVisible=ref(false);
var oldpwd=ref();
var newpwd=ref();

function pwdclear(){
  oldpwd.value=null;
  newpwd.value=null;
  pwdVisible.value=true;
}

function pwdsubmit(){
  proxy.$http.post("http://localhost:8000/api/changepwd/",{
    'userid':selected.value.userid,
    'oldpwd':oldpwd.value,
    'newpwd':newpwd.value,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==200&&selected.value.username==localStorage.getItem("username")){
      window.alert(res.data.msg);
      logout();
    }
    if(res.data.code==403) window.alert(res.data.msg);
  })
}

var changeVisible=ref(false);
var group=ref();
var groupcheck=ref();

function changeclear(row){
  changeVisible.value=true;
  selected.value=JSON.parse(JSON.stringify(row));
  getgroup();
}

function getgroup(){
  proxy.$http.post("http://localhost:8000/api/getgroupbyuser/",{
    'userid':selected.value.userid,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    else{
      group.value=res.data.data;
      groupcheck.value=res.data.group;
    }
  });
}

function editgroup(){
  proxy.$http.post("http://localhost:8000/api/editgroupbyuser/",{
    'userid':selected.value.userid,
    'group':JSON.stringify(groupcheck.value),
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  });
}

var deleteVisible=ref(false);

function deletesubmit(){
  proxy.$http.post("http://localhost:8000/api/deleteuser/",{
    'userid':selected.value.userid,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    getuser();
  });
}

function logout(){
  localStorage.removeItem('username');
  localStorage.removeItem('token');
  location.reload();
}

onMounted(()=>{
  getuser();
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