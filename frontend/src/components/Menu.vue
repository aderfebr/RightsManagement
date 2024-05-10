<template>
    <div class="main">
      <el-dialog
        v-model="editVisible"
        title="修改用户"
        width="500"
        :before-close="handleClose"
      >
        <span>ID:</span>
        <el-input 
          style="padding: 5px 0;"
          v-model="selected.id"
          disabled
        />
        <span>名称:</span>
        <el-input 
          style="padding: 5px 0;"
          v-model="selected.label"
        />
        <span>图标:</span>
        <el-input 
          style="padding: 5px 0;"
          v-model="selected.icon"
        />
        <span>路由:</span>
        <el-input 
          style="padding: 5px 0;"
          v-model="selected.index"
          disabled
        />
        <template #footer>
          <div class="dialog-footer">
            <el-button @click="editVisible = false">取消</el-button>
            <el-button type="success" @click="editVisible = false;editsubmit();">确认</el-button>
          </div>
        </template>
      </el-dialog>
      <Header></Header>
      <div class="title">菜单管理</div>
      <el-divider></el-divider>
      <el-table :data="tableData" style="width: 100%">
            <el-table-column label="ID">
              <template #default="scope">{{ scope.row.id }}</template>
            </el-table-column>
            <el-table-column label="名称">
              <template #default="scope">{{ scope.row.label }}</template>
            </el-table-column>
            <el-table-column label="图标">
              <template #default="scope">{{ scope.row.icon }}</template>
            </el-table-column>
            <el-table-column label="路由">
              <template #default="scope">{{ scope.row.index }}</template>
            </el-table-column>
            <el-table-column label="操作" width="300px">
              <template #default="scope">
                <el-button type="warning" @click="editclear(scope.row);">修改菜单</el-button>
              </template>
            </el-table-column>
          </el-table>
    </div>
</template>

<script setup>
import Header from '../components/Header.vue'
import { getCurrentInstance,onMounted,ref } from 'vue';
const {proxy} = getCurrentInstance()

var tableData=ref();

function getmenu(){
  proxy.$http.get("http://localhost:8000/api/getmenu/").then((res)=>{
    tableData.value=res.data;
  });
}

var editVisible=ref(false);
var selected=ref();

function editclear(row){
  editVisible.value=true;
  selected.value=JSON.parse(JSON.stringify(row))
}

function editsubmit(){
  proxy.$http.post("http://localhost:8000/api/editmenu/",{
    'id':selected.value.id,
    'label':selected.value.label,
    'icon':selected.value.icon,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    else location.reload();
  });
}

onMounted(()=>{
  getmenu();
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
.tree{
  font-size: 15px;
}
</style>