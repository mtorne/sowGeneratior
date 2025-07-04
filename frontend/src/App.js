import React, { useState } from 'react';

function App() {
  const [cliente, setCliente] = useState('');
  const [proyecto, setProyecto] = useState('');
  const [servicios, setServicios] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerar = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch('http://89.168.92.241:8000/generar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          cliente,
          proyecto,
          servicios_oci: servicios.split(',').map(s => s.trim())
        })
      });

      if (!response.ok) {
        throw new Error('Error generando el documento');
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'documento.docx';
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', fontFamily: 'Arial' }}>
      <h1>Generador de Documento Técnico (OCI)</h1>
      <form onSubmit={handleGenerar}>
        <label>Cliente:</label><br />
        <input value={cliente} onChange={e => setCliente(e.target.value)} required /><br /><br />

        <label>Proyecto:</label><br />
        <input value={proyecto} onChange={e => setProyecto(e.target.value)} required /><br /><br />

        <label>Servicios OCI (separados por coma):</label><br />
        <input value={servicios} onChange={e => setServicios(e.target.value)} required /><br /><br />

        <button type="submit" disabled={loading}>
          {loading ? 'Generando...' : 'Generar Documento'}
        </button>
      </form>
    </div>
  );
}

export default App;

