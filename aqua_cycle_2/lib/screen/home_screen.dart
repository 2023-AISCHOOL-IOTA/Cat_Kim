import 'package:flutter/material.dart';
import 'fish_page.dart';


class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF54b9de),
      appBar: AppBar(
        //leading: IconButton(icon: Icon(Icons.menu),onPressed: null,),
        actions: [
          IconButton(onPressed: null, icon: Icon(Icons.search)),
          //IconButton(onPressed: null, icon: Icon(Icons.person)),
        ],
        elevation: 0,
        backgroundColor: Color(0xFF54b9de),
        title: Image.asset('asset/img/aqua_cycle_logo_4.png'),
        centerTitle: true,
      ),
      drawer: Drawer(
        backgroundColor: Colors.white,
        child: ListView(
          children: [
            UserAccountsDrawerHeader(
              currentAccountPicture: CircleAvatar(
                backgroundImage: AssetImage('asset/img/mori.png'),
              ),
              accountName: Text('김고양이'),
              accountEmail: Text('cat_kim@naver.com'),
              onDetailsPressed: () {},
              decoration: BoxDecoration(
                color: Color(0xFF54b9de),
                borderRadius: BorderRadius.only(
                  bottomLeft: Radius.circular(10.0),
                  bottomRight: Radius.circular(10.0),
                ),
              ),
            ),

            ListTile(
              leading: Icon(Icons.home),
              iconColor: Color(0xFF54b9de),
              focusColor: Color(0xFF54b9de),
              title: Text('홈',style: TextStyle(color: Color(0xFF54b9de))),
              onTap: () {Navigator.pushNamed(context, '/');},
              trailing: Icon(Icons.navigate_next),
            ),
            ListTile(
              leading: Icon(Icons.person),
              iconColor: Color(0xFF54b9de),
              focusColor: Color(0xFF54b9de),
              title: Text('마이페이지',style: TextStyle(color: Color(0xFF54b9de))),
              onTap: () {Navigator.pushNamed(context, '/login');},
              trailing: Icon(Icons.navigate_next),
            ),
            ListTile(
              leading: Icon(Icons.sailing),
              iconColor: Color(0xFF54b9de),
              focusColor: Color(0xFF54b9de),
              title: Text('물고기사전',style: TextStyle(color: Color(0xFF54b9de))),
              onTap: () {Navigator.pushNamed(context, '/second');},
              trailing: Icon(Icons.navigate_next),
            ),
            ListTile(
              leading: Icon(Icons.grass),
              iconColor: Color(0xFF54b9de),
              focusColor: Color(0xFF54b9de),
              title: Text('식물사전',style: TextStyle(color: Color(0xFF54b9de))),
              onTap: () {Navigator.pushNamed(context, '/third');},
              trailing: Icon(Icons.navigate_next),
            ),
            ListTile(
              leading: Icon(Icons.settings),
              iconColor: Color(0xFF54b9de),
              focusColor: Color(0xFF54b9de),
              title: Text('환경설정',style: TextStyle(color: Color(0xFF54b9de))),
              onTap: () {},
              trailing: Icon(Icons.navigate_next),
            ),

          ],
        ),
      ),
      body: Center(
        child: Text(''),
      ),
    );
  }
}
