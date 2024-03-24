<template>
    <div class="main">
        <el-dialog
          v-model="editVisible"
          title="编辑信息"
          width="500"
          :before-close="handleClose"
        >
          <span>This is a message</span>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="editVisible = false">取消</el-button>
              <el-button type="success" @click="editVisible = false">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <el-dialog
          v-model="changeVisible"
          title="更改密码"
          width="500"
          :before-close="handleClose"
        >
          <br>
          <el-input
            v-model="oldpwd"
            type="password"
            placeholder="请输入旧密码"
            show-password
          />
          <br><br>
          <el-input
            v-model="newpwd"
            type="password"
            placeholder="请输入新密码"
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
              <el-button type="success" @click="deleteVisible = false">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <Header></Header>
        <div class="title">用户管理</div>
        <el-divider></el-divider>
        <div v-if="1">
          <el-row style="font-size: 25px;">
              <el-col :span="20"><el-input size="large" v-model="input" style="width: 300px"/>&ensp;<el-button type="primary">搜索&ensp;<el-icon><Search /></el-icon></el-button></el-col>
              <el-col :span="4" style="text-align: right;"><el-button type="success">新增&ensp;＋</el-button></el-col>
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
                <el-button type="warning" @click="editVisible=true;selected=scope.row;">编辑信息</el-button>
                <el-button type="primary" @click="changeclear();changeVisible=true;selected=scope.row;">更改密码</el-button>
                <el-button type="danger" @click="deleteVisible=true;selected=scope.row;">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div v-if="0" style="width: 100%;text-align: center;font-size: 25px;color: red;">未授权!</div>
    </div>
</template>

<script setup>
import { getCurrentInstance,onMounted, ref } from 'vue';
import Header from '../components/Header.vue'
const {proxy} = getCurrentInstance()

var selected=ref();

var editVisible=ref(false);

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
    else{
      localStorage.removeItem('username');
      localStorage.removeItem('token');
      location.reload();
    }
    selected=null;
  })
}

var deleteVisible=ref(false);

var tableData=ref()

function get_user(){
  proxy.$http.get("http://localhost:8000/api/user/").then((res)=>{
  tableData.value=res.data;
  });
}

onMounted(()=>{
  get_user();
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