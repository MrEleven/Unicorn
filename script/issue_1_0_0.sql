CREATE TABLE `goal` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` nvarchar(48) NOT NULL DEFAULT '' COMMENT '主题',
  `user_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'user_id',
  `status` int (10) unsigned NOT NULL DEFAULT '1' COMMENT '状态',
  `image` varchar(255) NOT NULL DEFAULT '' COMMENT 'image url',
  `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `description` nvarchar(255) NOT NULL DEFAULT '' COMMENT '描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COMMENT='目标';

CREATE TABLE `todo` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `goal_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '所属目标id',
  `user_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'user_id',
  `status` int (10) unsigned NOT NULL DEFAULT '1' COMMENT '状态',
  `name` nvarchar(48) NOT NULL DEFAULT '' COMMENT '主题',
  `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `close_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `note` nvarchar(255) NOT NULL DEFAULT '' COMMENT '备注信息',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COMMENT='待办事项';
