<aside class="main-sidebar sidebar-dark-primary elevation-4">
    <div class="sidebar">
        <div class="user-panel mt-3 pb-3 mb-3 d-flex">
            <div class="image">
                <img src="<?=$assetDir?>/img/user2-160x160.jpg" class="img-circle elevation-2" alt="User Image">
            </div>
            <div class="info">
                <a href="#" class="d-block">IFNMG</a>
            </div>
        </div>

        <nav class="mt-2">
            <?php
            echo \hail812\adminlte\widgets\Menu::widget([
                'items' => [
                    ['label' =>'Veículos', 'url' => ['/veiculo/index'], 'icon' =>'car'],
                    ['label' =>'Sobre', 'url' => ['/site/about'], 'icon' =>'info'],
                    ['label' => 'Sair', 'url' => ['site/logout'], 'icon' => 'sign-out-alt',  'visible' => Yii::$app->user->isGuest],
                ],
            ]);
            ?>
        </nav>
    </div>
</aside>