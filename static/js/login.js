window.addEventListener('load',()=>{
  // 我们需要获取两个切换按钮 因此需要到html结构中 定义特殊类名或id名
  const goSignIn = document.querySelector('#goSignIn');
  const goSignUp = document.querySelector('#goSignUp');
  // 获取被切换的样式类
  const container = document.querySelector('.container');
  // 添加点击事件
  goSignIn.addEventListener('click',()=>{
    container.classList.remove('switch');
  })
  goSignUp.addEventListener('click',()=>{
    container.classList.add('switch');
  })
  // 原理：通过点击goSignIn登录页按钮时 就删除switch这个类名 
  // 因为之前已经定义好了样式 删除switch类名 就会恢复成没有设置包含switch类
  // 反之点击goSignUp 就会添加switch类名 显示我们默认页面
  // 可以看到页面没有加过渡效果 继续前往css设置把！
})