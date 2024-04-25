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
            v-model="edited.groupid"
            disabled
          />
          <span>角色名:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="edited.groupname"
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
              <el-input size="large" v-model="input" style="width: 300px"/>&ensp;<el-button type="primary">搜索&ensp;<el-icon><Search /></el-icon></el-button>
          </el-row>
          <br>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="ID">
              <template #default="scope">{{ scope.row.groupid }}</template>
            </el-table-column>
            <el-table-column label="角色名">
              <template #default="scope">{{ scope.row.groupname }}</template>
            </el-table-column>
            <el-table-column label="操作">
              <template #default="scope">
                <el-button type="warning" @click="editclear(scope.row);">修改角色</el-button>
                <el-button type="primary" @click="changeclear(scope.row);">修改权限</el-button>
                <el-button type="danger" @click="deleteVisible=true;selected=scope.row;">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
    </div>
</template>

<script setup>
import Header from '../components/Header.vue'
import { getCurrentInstance,onMounted,ref } from 'vue';
const {proxy} = getCurrentInstance()

var tableData=ref();
var selected=ref();
var groupid=ref();
var rights=ref();
var rightscheck=ref();
var auth=ref(false);

function getgroup(){
  proxy.$http.post("http://localhost:8000/api/getgroup/",{
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==200){
      tableData.value=res.data.data;
      auth.value=true;
    }
  });
}

var edited=ref({});
var editVisible=ref(false);

function editclear(row){
  editVisible.value=true;
  selected.value=row;
  edited.value=JSON.parse(JSON.stringify(selected.value))
}

function editsubmit(){
  proxy.$http.post("http://localhost:8000/api/editgroup/",{
    'groupid':edited.value.groupid,
    'groupname':edited.value.groupname,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  });
  setTimeout(() => {
    getgroup();
  }, 200);
}

var changeVisible=ref(false);

function changeclear(row){
  changeVisible.value=true;
  groupid.value=row.groupid
  getrights();
}

function getrights(){
  proxy.$http.post("http://localhost:8000/api/getrights/",{
    'groupid':groupid.value,
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
    'groupid':groupid.value,
    'rights':JSON.stringify(rightscheck.value),
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  });
}

var deleteVisible=ref(false);

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