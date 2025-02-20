const tabs = Array.from(document.getElementsByClassName('tab'));
const tabsContent = Array.from(document.getElementsByClassName('tab__content'));

tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
        
        const tabActive = document.querySelector('.tab_active');       
        tabActive.className = 'tab';
        tabsContent[tabs.indexOf(tabActive)].className = 'tab__content';

        tab.className = 'tab tab_active';
        tabsContent[tabs.indexOf(tab)].className = 'tab__content tab__content_active';
    })
});