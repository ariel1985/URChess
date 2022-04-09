import 'package:flutter/material.dart';

void main() => runApp(App());

/// /////////////////////////////////////////////////////
/// #1 State variable - rebuilds screen on every call
/// /////////////////////////////////////////////////////
class App extends StatefulWidget {
  // const App({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() {
    return _AppState();
  }
}

/// /////////////////////////////////////////////////////
/// #2 The state - persistant (does not update screen)
/// /////////////////////////////////////////////////////

final _tokenController = TextEditingController();

class _AppState extends State<App> {
  /// To show user input as output - save state
  String output = 'No output to show ....';
  getInput() {
    setState(() {
      output = _tokenController.text;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('App |||')),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Container(
              width: double.infinity,
              child: Column(
                children: <Widget>[Text('TOKEN'), Text('Generate Token')],
              ),
            ),
            Container(
              child: Column(
                children: <Widget>[
                  TextField(
                    decoration: InputDecoration(labelText: 'Enter Token'),
                    controller: _tokenController,
                  ),
                  ElevatedButton(
                    onPressed: getInput,
                    child: Text("Submit"),
                  ),
                  Text(output),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
