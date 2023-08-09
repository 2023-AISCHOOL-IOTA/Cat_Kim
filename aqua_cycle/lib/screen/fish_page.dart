import 'package:flutter/material.dart';


class FishPage extends StatelessWidget {
  const FishPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF54b9de),
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Color(0xFF54b9de),
        title: Image.asset('asset/img/fish.png'),
        centerTitle: true,
      ),

    );
  }
}
