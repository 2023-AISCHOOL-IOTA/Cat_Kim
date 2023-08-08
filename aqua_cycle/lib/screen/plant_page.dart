import 'package:flutter/material.dart';


class PlantPage extends StatelessWidget {
  const PlantPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF54b9de),
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Color(0xFF54b9de),
        title: Image.asset('asset/img/plant.png'),
        centerTitle: true,
      ),

    );
  }
}
