CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255) not null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,
    bearing INT default NULL,
    current_status VARCHAR(20) default NULL,
    current_stop_sequence INT default NULL,
    direction_id INT default NULL,
    label VARCHAR(20) default NULL,
    occupancy_status VARCHAR(20) default NULL,
    speed INT default NULL,
    updated_at DATETIME default NULL
);

