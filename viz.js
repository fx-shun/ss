var spawn = require('child_process').spawn
py = spawn('python',['psapi.py'])

data = [1,2,3,4,5,6,7,8,9]
dataString = ''

py.stdout.on('data', function(data) {   
    dataString += data.toString() + "\r\n"
    console.log("%s\n", data.toString())
})
py.stdout.on('close', function() {
    console.log("On Close = ", dataString)
})
py.stdout.on('exit', function() {
    console.log("On Exit = ", dataString)
})

py.stdin.write(JSON.stringify(data)+"\n")
data = [5,6,7,8,9]
py.stdin.write(JSON.stringify(data)+"\n")
data = [7,8,9]
py.stdin.write(JSON.stringify(data)+"\n")
data = [5,9]
py.stdin.write(JSON.stringify(data)+"\n")

py.stdin.end()