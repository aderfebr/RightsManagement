<template>
    <div class="main">
        <el-dialog
          v-model="addVisible"
          title="添加角色"
          width="500"
          :before-close="handleClose"
        >
          <span>角色名:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.groupname"
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
          title="编辑信息"
          width="500"
          :before-close="handleClose"
        >
          <span>ID:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.groupid"
            disabled
          />
          <span>角色名:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="selected.groupname"
          />
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="editVisible = false">取消</el-button>
              <el-button type="success" @click="editVisible = false;editsubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <el-dialog
          v-model="changeVisible"
          title="修改权限"
          width="600"
          :before-close="handleClose"
        >
          <el-transfer
            v-model="rightscheck"
            :props="{
              key: 'rightsid',
              label: 'rightsname',
            }"
            :data="rights"
            :titles="['未分配权限', '已分配权限']"
          />
          <br><el-button type="success" @click="changeVisible = false;editrights()">确认&ensp;<el-icon><Check /></el-icon></el-button>
        </el-dialog>
        <el-dialog
          v-model="deleteVisible"
          title="删除"
          width="500"
          :before-close="handleClose"
        >
          <span>确定删除角色{{ selected.groupname }}?</span>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="deleteVisible = false">取消</el-button>
              <el-button type="success" @click="deleteVisible = false;deletesubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <Header></Header>
        <div class="title">角色管理</div>
        <el-divider></el-divider>
        <div v-if="auth">
          <el-row style="font-size: 25px;">
            <el-col :span="20"><el-input size="large" v-model="filter" placeholder="按角色名搜索" style="width: 300px"/>&ensp;<el-button type="primary" @click="getgroup">搜索&ensp;<el-icon><Search /></el-icon></el-button><el-button type="danger" @click="filter='';getgroup();">清空过滤&ensp;<el-icon><Close /></el-icon></el-button></el-col>
              <el-col :span="4" style="text-align: right;"><el-button type="success" @click="addclear">添加角色&ensp;+</el-button></el-col>
          </el-row>
          <br>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="ID">
              <template #default="scope">{{ scope.row.groupid }}</template>
            </el-table-column>
            <el-table-column label="角色名">
              <template #default="scope">{{ scope.row.groupname }}</template>
            </el-table-column>
            <el-table-column label="操作" width="300px">
              <template #default="scope">
                <el-button type="warning" @click="editclear(scope.row);">修改角色</el-button>
                <el-button type="primary" @click="changeclear(scope.row);">修改权限</el-button>
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
import Header from '../components/Header.vue'
import { getCurrentInstance,onMounted,ref } from 'vue';
const {proxy} = getCurrentInstance()

var tableData=ref();
var auth=ref(false);
var filter=ref();
var page=ref(1);
var total=ref(1);
var selected=ref();

function getgroup(){
  proxy.$http.post("http://localhost:8000/api/getgroup/",{
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

function addclear(){
  addVisible.value=true;
  selected.value={};
}

function addsubmit(){
  proxy.$http.post("http://localhost:8000/api/addgroup/",{
    'groupname':selected.value.groupname,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    else getgroup();
  });
}

var editVisible=ref(false);

function editclear(row){
  editVisible.value=true;
  selected.value=JSON.parse(JSON.stringify(row))
}

function editsubmit(){
  proxy.$http.post("http://localhost:8000/api/editgroup/",{
    'groupid':selected.value.groupid,
    'groupname':selected.value.groupname,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    else getgroup();
  });
}

var changeVisible=ref(false);
var rights=ref();
var rightscheck=ref();

function changeclear(row){
  changeVisible.value=true;
  selected.value=JSON.parse(JSON.stringify(row))
  getrights();
}

function getrights(){
  proxy.$http.post("http://localhost:8000/api/getrights/",{
    'groupid':selected.value.groupid,
    'token':localStorage.getItem("token"),
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
    'groupid':selected.value.groupid,
    'rights':JSON.stringify(rightscheck.value),
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  });
}

var deleteVisible=ref(false);

function deletesubmit(){
  proxy.$http.post("http://localhost:8000/api/deletegroup/",{
    'groupid':selected.value.groupid,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    else getgroup();
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