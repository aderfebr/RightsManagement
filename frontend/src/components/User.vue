<template>
    <div class="main">
        <Header></Header>
        <div class="title">用户管理</div>
        <el-divider></el-divider>
        <el-row style="font-size: 25px;">
            <el-col :span="20"><el-input size="large" v-model="input" style="width: 300px"/>&ensp;<el-button type="primary">搜索&ensp;<el-icon><Search /></el-icon></el-button></el-col>
            <el-col :span="4" style="text-align: right;"><el-button type="success">新增&ensp;＋</el-button></el-col>
        </el-row>
        <br>
        <el-table :data="tableData" style="width: 100%">
          <el-table-column label="ID">
            <template #default="scope">{{ scope.row.id }}</template>
          </el-table-column>
          <el-table-column label="用户名">
            <template #default="scope">{{ scope.row.name }}</template>
          </el-table-column>
          <el-table-column label="角色">
            <template #default="scope">{{ scope.row.role }}</template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="scope">
              <el-button type="warning" @click="handleEdit(scope.row)">编辑&ensp;<el-icon><Edit /></el-icon></el-button>
              <el-button type="danger" @click="handleDelete(scope.row)">删除&ensp;<el-icon><Delete /></el-icon></el-button>
            </template>
          </el-table-column>
        </el-table>
    </div>
</template>

<script setup>
import Header from '../components/Header.vue'

const handleEdit = (row) => {
  console.log(row)
}
const handleDelete = (row) => {
  console.log(row)
}
const tableData = [
  {
    id: 1,
    name: 'Tom',
    role: 'student',
  },
  {
    id: 2,
    name: 'Alice',
    role: 'teacher',
  },
]
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