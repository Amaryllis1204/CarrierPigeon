const tabList = document.querySelectorAll('.tab-menu');
const contentBoxList = document.querySelectorAll('.content-box');
for(let i = 0; i < tabList.length; i++){
    tabList[i].addEventListener('click', tabCheck, false);
}

function tabCheck(e){
    let num;
    if(!e.target.classList.contains('is-active')){
        for(let i = 0; i < tabList.length; i++){
            if(tabList[i].classList.contains('is-active')){
                tabList[i].classList.remove('is-active');
            }
        }   
        e.target.classList.add('is-active');
        for(let i = 0; i < tabList.length; i++){
            if(tabList[i].classList.contains('is-active')){
                num = i;
            }
        }
        contentCheck(num);
    }
}

function contentCheck(number){
    for(let i = 0; i < contentBoxList.length; i++){
        if(contentBoxList[i].classList.contains('is-active')){
            contentBoxList[i].classList.remove('is-active');
        }
    }
    contentBoxList[number].classList.add('is-active');
}