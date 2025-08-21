document.addEventListener('DOMContentLoaded', () => {
    // Referências aos elementos principais da página
    const menuPrincipal = document.getElementById('menu-principal');
    const formMedicoContainer = document.getElementById('form-medico-container');
    const formResponsavelContainer = document.getElementById('form-responsavel-container');
    const formBebeContainer = document.getElementById('form-bebe-container');

    // Referências aos botões do menu
    const btnShowMedico = document.getElementById('btn-show-medico');
    const btnShowResponsavel = document.getElementById('btn-show-responsavel');
    const btnShowBebe = document.getElementById('btn-show-bebe');
    
    // Referência a TODOS os botões de "Voltar"
    const btnsVoltar = document.querySelectorAll('.btn-voltar');

    // Agrupa todos os formulários para facilitar o gerenciamento
    const allForms = [formMedicoContainer, formResponsavelContainer, formBebeContainer];

    // Função para mostrar uma seção específica e esconder as outras
    function showSection(sectionToShow) {
        menuPrincipal.style.display = 'none'; // Esconde o menu
        allForms.forEach(form => form.style.display = 'none'); // Esconde todos os formulários
        
        if (sectionToShow) {
            sectionToShow.style.display = 'block'; // Mostra a seção desejada
        }
    }

    // Função para voltar ao menu principal
    function backToMenu() {
        allForms.forEach(form => form.style.display = 'none'); // Esconde todos os formulários
        menuPrincipal.style.display = 'block'; // Mostra o menu
    }

    // Adiciona os eventos de clique aos botões do menu
    btnShowMedico.addEventListener('click', () => showSection(formMedicoContainer));
    btnShowResponsavel.addEventListener('click', () => showSection(formResponsavelContainer));
    
    // Adiciona o evento de clique para todos os botões "Voltar"
    btnsVoltar.forEach(btn => btn.addEventListener('click', backToMenu));

    // Evento especial para o formulário de bebês, que precisa carregar dados
    btnShowBebe.addEventListener('click', async () => {
        try {
            // 1. Busca os dados dos médicos e responsáveis da nossa API no Flask
            const [medicosRes, responsaveisRes] = await Promise.all([
                fetch('/api/medicos'),
                fetch('/api/responsaveis')
            ]);

            const medicos = await medicosRes.json();
            const responsaveis = await responsaveisRes.json();

            // 2. Pega os elementos <select> do formulário
            const medicoSelect = document.getElementById('id_medico_select');
            const responsavelSelect = document.getElementById('id_responsavel_select');
            
            // 3. Limpa as opções antigas
            medicoSelect.innerHTML = '<option value="" disabled selected>Selecione um médico...</option>';
            responsavelSelect.innerHTML = '<option value="" disabled selected>Selecione um responsável...</option>';

            // 4. Preenche o select de médicos
            medicos.forEach(medico => {
                const option = new Option(medico[1], medico[0]); // (texto, valor)
                medicoSelect.add(option);
            });

            // 5. Preenche o select de responsáveis
            responsaveis.forEach(responsavel => {
                const option = new Option(responsavel[1], responsavel[0]);
                responsavelSelect.add(option);
            });

            // 6. Finalmente, mostra o formulário do bebê
            showSection(formBebeContainer);

        } catch (error) {
            console.error('Erro ao buscar dados para o formulário de bebês:', error);
            alert('Não foi possível carregar os dados. Verifique o console para mais detalhes.');
        }
    });
});
