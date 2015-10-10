CREATE TABLE `marker` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(48) NOT NULL DEFAULT '' COMMENT '主题',
  `marker` varchar(1024) NOT NULL DEFAULT '' COMMENT '签到内容',
  `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='签到';


CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `phone` varchar(16) NOT NULL DEFAULT '' COMMENT '手机号码',
  `email` varchar(40) NOT NULL DEFAULT '' COMMENT 'email',
  `nickname` varchar(32) NOT NULL DEFAULT '' COMMENT '昵称',
  `avatar_url` varchar(255) NOT NULL DEFAULT '' COMMENT 'avatar url',
  `password` char(32) NOT NULL DEFAULT '' COMMENT '密码',
  `regist_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息';

