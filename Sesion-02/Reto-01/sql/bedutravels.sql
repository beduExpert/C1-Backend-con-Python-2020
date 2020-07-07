DROP DATABASE IF EXISTS BeduTravels;
CREATE DATABASE BeduTravels;
GRANT ALL PRIVILEGES ON BeduTravels.* TO BeduTravels@'%' IDENTIFIED BY 'BeduTravels';
GRANT ALL PRIVILEGES ON BeduTravels.* TO BeduTravels@'localhost' IDENTIFIED BY 'BeduTravels';
