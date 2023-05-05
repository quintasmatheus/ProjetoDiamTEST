class HoverAnim {
  constructor(el){
    this.el = el;
    this.hover = false;
    this.calculatePosition();
    this.attachEventListener();
  }

  attachEventListener() {
    window.addEventListener('mousemove', e => this.onMouseMove(e));
    window.addEventListener('resize', e => this.calculatePosition(e));
  }

  calculatePosition() {
    gsap.set(this.el, {
      x: 0,
      y: 0,
      scale: 1
    });
    const box = this.el.getBoundingClientRect();
    this.x = box.left + (box.width * 0.5);
    this.y = box.top + (box.height * 0.5);
    this.width = box.width;
    this.height = box.height;
  }

  onMouseMove(e){
    let hover = false;
    let hoverArea = (this.hover ? 0.7 : 0.5);
    let x = e.clientX - this.x;
    let y = e.clientY - this.y;
    let distance = Math.sqrt( x*x + y*y );
    if (distance < (this.width * hoverArea)) {
       hover = true;
        if (!this.hover) {
          this.hover = true;
        }
        this.onHover(e.clientX, e.clientY);
    }

    if(!hover && this.hover) {
      this.onLeave();
      this.hover = false;
    }
  }

  onHover(x, y) {
    gsap.to(this.el,  {
      x: (x - this.x) * 0.4,
      y: (y - this.y) * 0.4,
      scale: 1.15,
      ease: 'power2.out',
      duration: 0.4
    });
    this.el.style.zIndex = 10;
  }

  onLeave() {
    gsap.to(this.el, {
      x: 0,
      y: 0,
      scale: 1,
      ease: 'elastic.out(2.5, 0.5)',
      duration: 1
    });
    this.el.style.zIndex = 1;
  }
}

const titulo = document.getElementById("titulo");
new HoverAnim(titulo);

//////////////////////////////////////////////////////////////////////
//adicionar class active

const hamMenu = document.querySelector('.hamburger-menu')
const offScreenMenu = document.querySelector('.off-screen-menu');

hamMenu.addEventListener('click', ()=>{
  hamMenu.classList.toggle('active');
  offScreenMenu.classList.toggle('active');
} )

//////////////////////////////////////////////////////////////////////
const table = document.querySelector('#anuncios_table table');
const tbody = document.querySelector('#anuncios_table tbody');

// Função para ajustar a altura da tabela
function ajustarAlturaTabela() {
  if (table && tbody) {
    // Altura da tabela é a altura do tbody
    const alturaTabela = tbody.offsetHeight;
    // Ajusta a altura da tabela
    table.style.height = `${alturaTabela}px`;
  }
}

// Chama a função quando a página carrega
window.addEventListener('load', ajustarAlturaTabela);

// Chama a função sempre que a página é redimensionada
window.addEventListener('resize', ajustarAlturaTabela);


//////////////////////////////////////////////////////////////////////
// searchbar implementation

// const searchForm = document.getElementById('searchForm');
// const searchButton = document.getElementById('search_button');
//
// searchForm.addEventListener('submit', (event) => {
//         event.preventDefault(); // impede o envio do formulário padrão
//         const formData = new FormData(searchForm); // obtém os dados do formulário
//         const partida = formData.get('partida');
//         const chegada = formData.get('chegada');
//         const url = `./search/?partida=${partida}&chegada=${chegada}`; // constrói a URL de pesquisa
//         fetch(url)
//             .then(response => response.json())
//             .then(data => {
//                 // atualiza a tabela de boleias com os dados recebidos
//                 const table = document.getElementById('boleiaTable');
//                 table.innerHTML = ''; // limpa a tabela existente
//                 data.forEach(boleia => {
//                     const row = table.insertRow();
//                     row.insertCell().innerHTML = boleia.id;
//                     row.insertCell().innerHTML = boleia.partida;
//                     row.insertCell().innerHTML = boleia.chegada;
//                     // adicione outras células da tabela, se necessário
//                 });
//             })
//             .catch(error => console.error(error));
//     });



