CREATE TABLE `marker` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(48) NOT NULL DEFAULT '' COMMENT '主题',
  `marker` varchar(1024) NOT NULL DEFAULT '' COMMENT '签到内容',
  `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='签到'


CREATE TABLE `member` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `login_name` varchar(16) NOT NULL DEFAULT '' COMMENT '登陆用户名',
  `nick_name` varchar(32) NOT NULL DEFAULT '' COMMENT '昵称',
  `password` char(32) NOT NULL DEFAULT '' COMMENT '密码',
  `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `last_login_ip` varchar(15) NOT NULL DEFAULT '' COMMENT '最近登陆ip',
  `last_login_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户'

