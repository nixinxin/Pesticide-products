/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost:3306
 Source Schema         : chartsite

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 27/05/2018 21:24:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for nongyao
-- ----------------------------
DROP TABLE IF EXISTS `nongyao`;
CREATE TABLE `nongyao`  (
  `province` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `company` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `category` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_type` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `add_time` date DEFAULT NULL,
  `expired` date DEFAULT NULL,
  PRIMARY KEY (`title`, `product_id`, `company`, `province`, `category`, `product_type`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
