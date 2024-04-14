<body>

<h1>StockControl</h1>

<h2>Descripción del Proyecto</h2>
<p>StockControl es una aplicación construida con Django que permite agregar nuevos clientes y proveedores y listarlos. Esta aplicación proporciona una solución para gestionar productos y proveedores de una manera eficiente.</p>

<p>User: admin</p>
<p>Password: admin</p>

<h2>Requerimientos</h2>
<p>Se requiere crear un proyecto llamado StockControl con las siguientes especificaciones:</p>
<ul>
    <li>Agregar una app llamada compra.</li>
    <li>Dentro de la app compra, se deben agregar los modelos Producto y Proveedor con los campos requeridos.</li>
    <li>El modelo Producto debe estar relacionado con el modelo Proveedor utilizando una relación de clave foránea.</li>
    <li>Crear y ejecutar el archivo de migración para aplicar los cambios en la base de datos.</li>
</ul>

<h2>Funcionalidades</h2>
<p>La aplicación StockControl proveer las siguientes funcionalidades:</p>

<h3>Proveedor</h3>
<ul>
    <li>Agregar un nuevo Proveedor con los siguientes detalles:</li>
    <ul>
        <li>Nombre (texto)</li>
        <li>Apellido (texto)</li>
        <li>DNI (integer)</li>
    </ul>
    <li>Se proporciona un formulario para agregar un nuevo proveedor.</li>
    <li>Se muestra el listado de proveedores con la opcion de eliminar y editar, a través de una tabla HTML en la vista /proveedores.</li>
</ul>

<h3>Producto</h3>
<ul>
    <li>Agregar un nuevo Producto con los siguientes detalles:</li>
    <ul>
        <li>Nombre (texto)</li>
        <li>Precio (float o integer)</li>
        <li>Stock actual (integer)</li>
    </ul>
    <li>Se proporciona un formulario para agregar un nuevo producto.</li>
</ul>

<h3>Listado de Productos</h3>
<ul>
    <li>Se lista todos los productos registrados en la base de datos.</li>
    <li>Se muestra el listado de productos con la opcion de eliminar y editar, a través de una tabla HTML en la vista /productos.</li>
</ul>

<h2>Acciones</h2>
<p>Las acciones disponibles en la aplicación StockControl son:</p>
<ul>
    <li>Listar todos los productos registrados en la base de datos.</li>
    <li>Permitir agregar un nuevo producto.</li>
    <li>Permitir agregar un nuevo proveedor.</li>
    <li>Disponer del modelo del producto y del proveedor en el panel de administración de Django.</li>
</ul>

<h2>Uso</h2>
<p>La aplicación StockControl permite almacenar y gestionar productos y proveedores de manera efectiva, brindando una interfaz intuitiva para agregar y listar información. Utiliza las funcionalidades disponibles para agregar nuevos elementos y consultar la lista de productos registrados.</p>

<p>¡Gracias por utilizar StockControl para administrar tus productos y proveedores de manera eficiente!</p>

</body>
</html>
