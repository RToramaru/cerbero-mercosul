<?php
use \hail812\adminlte\widgets\Menu;
?>

<aside class="main-sidebar sidebar-dark-primary elevation-4">
    <!-- Brand Logo -->
    <a href="index3.html" class="brand-link">
        <span class="brand-text font-weight-light">Cérbero</span>
    </a>

    <div class="sidebar">
        <nav class="mt-2">
            <?php
            echo Menu::widget([
                'items' => [
                    ['label' => 'Principal', 'url' => ['site/index'], 'icon' => 'home'],
                    ['label' => 'Veiculos', 'url' => ['veiculo/index'], 'icon' => 'car'],
                    ['label' => 'Usuários', 'url' => ['usuarios/index'], 'icon' => 'user'],
                    ['label' => 'Sobre', 'url' => ['site/about'], 'icon' => 'info'],
                ],
            ]);
            ?>
        </nav>
        <!-- /.sidebar-menu -->
    </div>
    <!-- /.sidebar -->
</aside>