import 'package:flutter/material.dart';

class Login extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('로그인'),
        backgroundColor: Color(0xFF54b9de),
      ),

      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextFormField(
              decoration: InputDecoration(labelText: '이메일'),
            ),
            TextFormField(
              decoration: InputDecoration(labelText: '비밀번호'),
              obscureText: true,
            ),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
              ElevatedButton(
                style: ElevatedButton.styleFrom(
                  primary: Color(0xFF54b9de),
                ),
                onPressed: () {
                  // 로그인 로직 구현
                },
                child: Text('로그인'),
              ),

              SizedBox(width: 20,),

              ElevatedButton(
                style: ElevatedButton.styleFrom(
                  primary: Color(0xFF54b9de),
                ),
                onPressed: () {
                  // 로그인 로직 구현
                },
                child: Text('회원가입'),
              ),
            ],
            ),

          ],
        ),
      ),
    );
  }
}