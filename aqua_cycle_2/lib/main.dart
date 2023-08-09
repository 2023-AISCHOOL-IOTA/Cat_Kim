import 'package:aqua_cycle_2/screen/home_screen.dart';
import 'package:aqua_cycle_2/screen/login.dart';
import 'package:aqua_cycle_2/screen/plant_page.dart';
import 'package:aqua_cycle_2/screen/fish_page.dart';
import 'package:flutter/material.dart';


void main() {
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      home: HomeScreen(),
      routes: {
        '/second' : (context) => FishPage(),
        '/third' : (context) => PlantPage(),
        '/login' : (context) => Login(),


      },
    ),
  );
}


