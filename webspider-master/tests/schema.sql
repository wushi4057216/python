-- CREATE DATABASE `spider` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `job` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `lagou_job_id`INT UNSIGNED NOT NULL COMMENT '拉勾所使用的职位id',
  `city_id`     INT UNSIGNED NOT NULL COMMENT '城市 id',
  `company_id`  INT UNSIGNED NOT NULL COMMENT '公司 id',
  `title`       VARCHAR(64) NOT NULL COMMENT '职位标题',
  `work_year`   TINYINT NOT NULL DEFAULT 0 COMMENT '工作年限要求',
  `department`  VARCHAR(64) NOT NULL DEFAULT '' COMMENT '招聘部门',
  `salary`      VARCHAR(32) NOT NULL DEFAULT '' COMMENT '薪水',
  `education`   TINYINT NOT NULL DEFAULT 0 COMMENT '教育背景要求',
  `nature`      TINYINT NOT NULL DEFAULT 0 COMMENT '工作性质',
  `description` VARCHAR(2048) NOT NULL DEFAULT '' COMMENT '额外描述',
  `advantage`   VARCHAR(256) NOT NULL DEFAULT '' COMMENT '职位优势',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY (`lagou_job_id`),
  KEY `idx_company_id` (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='职位表';


CREATE TABLE IF NOT EXISTS `company` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `lagou_company_id` INT UNSIGNED NOT NULL COMMENT '拉勾所使用的公司id',
  `city_id`     INT UNSIGNED NOT NULL COMMENT '所在城市 id',
  `shortname`   VARCHAR(64) NOT NULL COMMENT '公司名称',
  `fullname`    VARCHAR(128) NOT NULL COMMENT '公司全称',
  `finance_stage` TINYINT NOT NULL DEFAULT 0 COMMENT '融资阶段',
  `size`        TINYINT NOT NULL DEFAULT 0 COMMENT '公司规模',
  `address`     VARCHAR(128) NOT NULL DEFAULT '' COMMENT '公司地址',
  `features`    VARCHAR(128) NOT NULL DEFAULT '' COMMENT '公司特点',
  `process_rate` TINYINT NOT NULL DEFAULT 0  COMMENT '简历处理率',
  `introduce`   VARCHAR(2048) NOT NULL DEFAULT '' COMMENT '公司简介',
  `advantage`   VARCHAR(256) NOT NULL DEFAULT '' COMMENT '公司优势',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY (`lagou_company_id`),
  KEY `idx_city_id` (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='公司表';


CREATE TABLE IF NOT EXISTS `city` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name`        VARCHAR(64) NOT NULL COMMENT '城市名',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='城市表';


CREATE TABLE IF NOT EXISTS `industry` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name`        VARCHAR(64) NOT NULL COMMENT '行业名称',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4  COMMENT='行业表';


CREATE TABLE IF NOT EXISTS `company_industry` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `company_id`  INT UNSIGNED NOT NULL COMMENT '公司 id',
  `industry_id` INT UNSIGNED NOT NULL COMMENT '行业 id',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY(`company_id`, `industry_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='公司行业表';


-- 拉勾预置行业类型
INSERT INTO `industry` (`id`, `name`)
VALUES
(24,'移动互联网'),
(25,'电子商务'),
(26,'社交网络'),
(27,'企业服务'),
(28,'O2O'),
(29,'教育'),
(31,'游戏'),
(32,'旅游'),
(33,'金融'),
(34,'医疗健康'),
(35,'生活服务'),
(38,'信息安全'),
(41,'数据服务'),
(43,'广告营销'),
(45,'文化娱乐'),
(47,'硬件'),
(48,'分类信息'),
(49,'招聘'),
(10594,'其他');


CREATE TABLE IF NOT EXISTS `keyword` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name`        VARCHAR(64) NOT NULL COMMENT '关键词名称',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='关键词';


CREATE TABLE IF NOT EXISTS `job_keyword` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `job_id`      INT NOT NULL COMMENT '工作 id',
  `keyword_id`  INT NOT NULL COMMENT '关键词 id',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY(`job_id`, `keyword_id`),
  KEY `idx_keyword_id` (`keyword_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='职位关键词';


CREATE TABLE IF NOT EXISTS `jobs_count` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `date`        INT NOT NULL COMMENT '日期',
  `keyword_id`  INT NOT NULL COMMENT '关键词 id',
  `all_city`    INT NOT NULL DEFAULT 0 COMMENT '全国岗位数量',
  `beijing`     INT NOT NULL DEFAULT 0 COMMENT '北京岗位数量',
  `guangzhou`   INT NOT NULL DEFAULT 0 COMMENT '广州岗位数量',
  `shenzhen`    INT NOT NULL DEFAULT 0 COMMENT '深圳岗位数量',
  `shanghai`    INT NOT NULL DEFAULT 0 COMMENT '上海岗位数量',
  `hangzhou`    INT NOT NULL DEFAULT 0 COMMENT '杭州岗位数量',
  `chengdu`     INT NOT NULL DEFAULT 0 COMMENT '成都岗位数量',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY(`date`, `keyword_id`),
  KEY `idx_keyword_id` (`keyword_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='职位每日数量统计';


CREATE TABLE IF NOT EXISTS `keyword_statistic` (
  `id`          INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `keyword_id`  INT UNSIGNED NOT NULL COMMENT '关键词 id',
  `educations`  VARCHAR(2048) NOT NULL DEFAULT '' COMMENT '教育背景要求情况',
  `city_jobs_count`VARCHAR(2048) NOT NULL DEFAULT '' COMMENT '城市职位数量情况',
  `salary`      VARCHAR(2048) NOT NULL DEFAULT '' COMMENT '薪水分布情况',
  `financing_stage` VARCHAR(2048) NOT NULL DEFAULT '' COMMENT '公司融资阶段情况',
  `work_years`  VARCHAR(2048) NOT NULL DEFAULT '' COMMENT '要求的工作年限情况',
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  UNIQUE KEY(`keyword_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='关键词分析表' COMMENT='关键词分析';
