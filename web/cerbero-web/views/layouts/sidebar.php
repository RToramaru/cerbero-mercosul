<?php

use \hail812\adminlte\widgets\Menu;
use yii\bootstrap5\Nav;
use yii\bootstrap5\Html;
?>

<aside class="main-sidebar sidebar-dark-primary elevation-4">
    <!-- Brand Logo -->
    <div>
        <span class="text-light brand-link">Cérbero</span>
    </div>

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
            echo Nav::widget([
                'options' => ['class' => 'mt-2'],
                'items' => [
                    Yii::$app->user->isGuest
                        ? ['label' => 'Login', 'url' => ['/site/login']]
                        : '<li class="mt-2">'
                        . Html::beginForm(['/site/logout'])
                        . Html::submitButton(
                            'Sair (' . Yii::$app->user->identity->nome . ')',
                            ['class' => 'nav-link btn btn-danger text-light']
                        )
                        . Html::endForm()
                        . '</li>'
                ]
            ]);
            ?>
        </nav>
        <!-- /.sidebar-menu -->
    </div>
    <!-- /.sidebar -->
</aside>