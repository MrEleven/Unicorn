alter table `marker` add column `user_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'user_id' after `title`;
update marker set user_id = 1 where user_id = 0 or user_id is null;