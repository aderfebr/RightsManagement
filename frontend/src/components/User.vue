<template>
    <div class="main">
        <el-dialog
          v-model="editVisible"
          title="编辑信息"
          width="500"
          :before-close="handleClose"
        >
          <span>ID:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="edited.userid"
            disabled
          />
          <span>用户名:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="edited.username"
          />
          <span>角色:</span>
          <el-select
            style="padding: 5px 0;"
            v-model="edited.groupid"
            placeholder=""
          >
            <el-option
              v-for="item in options"
              :key="item.groupid"
              :label="item.groupname"
              :value="item.groupid"
            />
          </el-select>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="editVisible = false">取消</el-button>
              <el-button type="success" @click="editVisible = false;editsubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <el-dialog
          v-model="changeVisible"
          title="更改密码"
          width="500"
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
              <el-button @click="changeVisible = false">取消</el-button>
              <el-button type="success" @click="changeVisible = false;changesubmit();">确认</el-button>
            </div>
          </template>
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
              <el-input size="large" v-model="input" style="width: 300px"/>&ensp;<el-button type="primary">搜索&ensp;<el-icon><Search /></el-icon></el-button>
          </el-row>
          <br>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="ID">
              <template #default="scope">{{ scope.row.userid }}</template>
            </el-table-column>
            <el-table-column label="用户名">
              <template #default="scope">{{ scope.row.username }}</template>
            </el-table-column>
            <el-table-column label="角色">
              <template #default="scope">{{ scope.row.groupname }}</template>
            </el-table-column>
            <el-table-column label="操作">
              <template #default="scope">
                <el-button type="warning" @click="editVisible=true;selected=scope.row;editclear();">编辑信息</el-button>
                <el-button type="primary" @click="changeVisible=true;selected=scope.row;changeclear();">更改密码</el-button>
                <el-button type="danger" @click="deleteVisible=true;selected=scope.row;">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div v-if="!auth" style="width: 100%;text-align: center;font-size: 25px;color: red;">未授权!</div>
    </div>
</template>

<script setup>
import { getCurrentInstance,onMounted, ref } from 'vue';
import Header from '../components/Header.vue'
const {proxy} = getCurrentInstance()

var options=ref();
var tableData=ref()
var auth=ref(false)

function getuser(){
  proxy.$http.post("http://localhost:8000/api/getuser/",{
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    tableData.value=res.data.data;
    if(res.data.code==200) auth.value=true;
  });
}

function getgroup(){
  proxy.$http.get("http://localhost:8000/api/getgroup/").then((res)=>{
    options.value=res.data.data;
  })
}

var selected=ref();

var edited=ref({});
var editVisible=ref(false);
function editclear(){
  edited.value=JSON.parse(JSON.stringify(selected.value))
}
function editsubmit(){
  proxy.$http.post("http://localhost:8000/api/edituser/",{
    'userid':edited.value.userid,
    'username':edited.value.username,
    'groupid':edited.value.groupid,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  });
  setTimeout(() => {
    getuser();
  }, 200);
}

var changeVisible=ref(false);
var oldpwd=ref();
var newpwd=ref();
function changeclear(){
  oldpwd.value=null;
  newpwd.value=null;
}
function changesubmit(){
  proxy.$http.post("http://localhost:8000/api/changepwd/",{
    'userid':selected.value.userid,
    'oldpwd':oldpwd.value,
    'newpwd':newpwd.value,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  })
}

var deleteVisible=ref(false);
function deletesubmit(){
  proxy.$http.post("http://localhost:8000/api/deleteuser/",{
    'userid':selected.value.userid,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  });
  location.reload();
}

onMounted(()=>{
  getuser();
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