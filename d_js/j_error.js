class MyError extends Error{}

const studyMyError = () => {
    console.log("내가 만든 예외 발생");
    throw new MyError("내가 만든 예외");
}

try{
    console.log("try block")
    // console.log(notDefined)
    studyMyError()
}catch(error){
    console.log("catch block")
    console.error(error)
}finally{
    console.log("finally block")
}

