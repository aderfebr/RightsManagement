DROP TABLE IF EXISTS `group`,`group_rights`,`menu`,`rights`,`token`,`user`,`user_group`;
CREATE TABLE `group` (
  `groupid` int NOT NULL AUTO_INCREMENT,
  `groupname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`groupid`)
);
CREATE TABLE `group_rights` (
  `id` int NOT NULL AUTO_INCREMENT,
  `groupid` int DEFAULT NULL,
  `rightsid` int DEFAULT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE `menu` (
  `id` int NOT NULL,
  `label` varchar(45) DEFAULT NULL,
  `icon` varchar(45) DEFAULT NULL,
  `index` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE `rights` (
  `rightsid` int NOT NULL,
  `rightsname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`rightsid`)
);
CREATE TABLE `token` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(45) DEFAULT NULL,
  `value` varchar(45) DEFAULT NULL,
  `expire_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE `user` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userid`)
);
CREATE TABLE `user_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` int DEFAULT NULL,
  `groupid` int DEFAULT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO `rightsmanagement`.`menu` (`id`, `label`, `icon`, `index`) VALUES ('1', '主页', 'HomeFilled', '/home');
INSERT INTO `rightsmanagement`.`menu` (`id`, `label`, `icon`, `index`) VALUES ('2', '用户管理', 'UserFilled', '/user');
INSERT INTO `rightsmanagement`.`menu` (`id`, `label`, `icon`, `index`) VALUES ('3', '角色管理', 'MoreFilled', '/group');
INSERT INTO `rightsmanagement`.`menu` (`id`, `label`, `icon`, `index`) VALUES ('4', '菜单管理', 'Operation', '/menu');
INSERT INTO `rightsmanagement`.`group` (`groupname`) VALUES ('admin');
INSERT INTO `rightsmanagement`.`group` (`groupname`) VALUES ('teacher');
INSERT INTO `rightsmanagement`.`group` (`groupname`) VALUES ('student');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('1', '查询用户');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('2', '增加用户');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('3', '修改用户');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('4', '修改用户角色');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('5', '删除用户');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('6', '查询角色');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('7', '增加角色');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('8', '修改角色');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('9', '修改角色权限');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('10', '删除角色');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('11', '修改菜单');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '1');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '2');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '3');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '4');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '5');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '6');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '7');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '8');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '9');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '10');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '11');