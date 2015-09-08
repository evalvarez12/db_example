# main.go
package main

import (
  "upper.io/db"
  "upper.io/db/mysql"
)

type ConnectionURL struct {
  User     string
  Password string
  Address  db.Address
  Database string
  Options  map[string]string
}


var settings = mysql.ConnectionURL{
  Address:  db.Host("localhost"), // MySQL server IP or name.
  Database: "upper_tests",            // Database name.
  User:     "upperio",             // Optional user name.
  Password: "upperpass",             // Optional user password.
}